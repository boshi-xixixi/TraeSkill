#!/usr/bin/env python3
"""
Skill 质量检查脚本
自动验证 Skill 目录结构、SKILL.md 格式和命名规范
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ValidationResult:
    """验证结果"""
    skill_name: str
    skill_path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    
    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0


class SkillValidator:
    """Skill 质量验证器"""
    
    VALID_NAME_PATTERN = re.compile(r'^\d{2}_[A-Za-z]+_[A-Za-z]+$')
    FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    
    def __init__(self, skills_dir: Path):
        self.skills_dir = skills_dir
    
    IGNORED_DIRS = {"scripts", "assets", "references", "__pycache__", ".git"}
    
    def validate_all(self) -> list[ValidationResult]:
        """验证所有 Skill"""
        results = []
        
        for skill_dir in sorted(self.skills_dir.iterdir()):
            if skill_dir.is_dir() and not skill_dir.name.startswith('.'):
                if skill_dir.name in self.IGNORED_DIRS:
                    continue
                if not (skill_dir / "SKILL.md").exists():
                    continue
                result = self.validate_skill(skill_dir)
                results.append(result)
        
        return results
    
    def validate_skill(self, skill_dir: Path) -> ValidationResult:
        """验证单个 Skill"""
        result = ValidationResult(
            skill_name=skill_dir.name,
            skill_path=skill_dir
        )
        
        self._check_directory_naming(skill_dir, result)
        self._check_skill_md(skill_dir, result)
        self._check_agents_md(skill_dir, result)
        self._check_directory_structure(skill_dir, result)
        
        return result
    
    def _check_directory_naming(self, skill_dir: Path, result: ValidationResult) -> None:
        """检查目录命名规范"""
        name = skill_dir.name
        
        if not self.VALID_NAME_PATTERN.match(name):
            result.errors.append(
                f"目录命名不符合规范: {name} (期望格式: XX_Category_Name)"
            )
        
        parts = name.split('_')
        if len(parts) >= 1:
            try:
                num = int(parts[0])
                if num not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99]:
                    result.warnings.append(
                        f"层级编号 {num} 不在标准范围内 (0-10, 99)"
                    )
            except ValueError:
                result.errors.append(f"目录编号不是有效数字: {parts[0]}")
    
    def _check_skill_md(self, skill_dir: Path, result: ValidationResult) -> None:
        """检查 SKILL.md 文件"""
        skill_md = skill_dir / "SKILL.md"
        
        if not skill_md.exists():
            result.errors.append("缺少 SKILL.md 文件")
            return
        
        content = skill_md.read_text(encoding="utf-8")
        
        frontmatter_match = self.FRONTMATTER_PATTERN.match(content)
        if not frontmatter_match:
            result.errors.append("SKILL.md 缺少 YAML frontmatter")
            return
        
        frontmatter = frontmatter_match.group(1)
        
        if "name:" not in frontmatter:
            result.errors.append("SKILL.md frontmatter 缺少 'name' 字段")
        
        if "description:" not in frontmatter:
            result.errors.append("SKILL.md frontmatter 缺少 'description' 字段")
        else:
            desc_match = re.search(r'description:\s*(.+?)(?:\n|$)', frontmatter)
            if desc_match:
                desc = desc_match.group(1).strip()
                if len(desc) < 20:
                    result.warnings.append(
                        f"description 过短 ({len(desc)} 字符)，建议至少 20 字符"
                    )
    
    def _check_agents_md(self, skill_dir: Path, result: ValidationResult) -> None:
        """检查 AGENTS.md 文件"""
        agents_md = skill_dir / "AGENTS.md"
        
        if not agents_md.exists():
            result.warnings.append("缺少 AGENTS.md 文件 (建议添加智能体角色定义)")
            return
        
        content = agents_md.read_text(encoding="utf-8")
        
        frontmatter_match = self.FRONTMATTER_PATTERN.match(content)
        if not frontmatter_match:
            result.errors.append("AGENTS.md 缺少 YAML frontmatter")
            return
        
        frontmatter = frontmatter_match.group(1)
        
        if "name:" not in frontmatter:
            result.errors.append("AGENTS.md frontmatter 缺少 'name' 字段")
        
        if "description:" not in frontmatter:
            result.errors.append("AGENTS.md frontmatter 缺少 'description' 字段")
    
    def _check_directory_structure(self, skill_dir: Path, result: ValidationResult) -> None:
        """检查目录结构"""
        expected_dirs = ["references", "scripts", "assets"]
        
        has_any_resource = any(
            (skill_dir / d).exists() for d in expected_dirs
        )
        
        if not has_any_resource:
            result.warnings.append(
                "缺少资源目录 (references/scripts/assets)，建议添加"
            )


def print_results(results: list[ValidationResult], verbose: bool = False) -> int:
    """打印验证结果"""
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    total_errors = sum(len(r.errors) for r in results)
    total_warnings = sum(len(r.warnings) for r in results)
    
    print("\n" + "=" * 60)
    print("📊 Skill 质量检查报告")
    print("=" * 60)
    print(f"总计: {total} 个 Skill")
    print(f"✅ 通过: {valid} 个")
    print(f"❌ 失败: {total - valid} 个")
    print(f"🔴 错误: {total_errors} 个")
    print(f"🟡 警告: {total_warnings} 个")
    print("=" * 60)
    
    for result in results:
        if result.errors or result.warnings or verbose:
            print(f"\n📁 {result.skill_name}")
            
            for error in result.errors:
                print(f"   🔴 {error}")
            
            for warning in result.warnings:
                print(f"   🟡 {warning}")
    
    print("\n" + "=" * 60)
    
    return 0 if total_errors == 0 else 1


def main():
    parser = argparse.ArgumentParser(description="Skill 质量检查脚本")
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path(__file__).parent.parent,
        help="Skills 目录路径"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="显示详细信息"
    )
    
    args = parser.parse_args()
    
    if not args.skills_dir.exists():
        print(f"❌ Skills 目录不存在: {args.skills_dir}")
        return 1
    
    validator = SkillValidator(args.skills_dir)
    results = validator.validate_all()
    
    return print_results(results, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
