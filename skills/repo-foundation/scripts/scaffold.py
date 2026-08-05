#!/usr/bin/env python3
"""
Repo Foundation Scaffolder
Copies the foundation-template/ into a new project directory and
replaces {{PROJECT_NAME}} / {{SCAFFOLD_DATE}} placeholders.

Usage:
    python scaffold.py --name my-new-platform --target /path/to/parent/dir
"""

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent / "assets" / "foundation-template"


def replace_placeholders(root: Path, project_name: str, scaffold_date: str):
    for path in root.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            new_text = text.replace("{{PROJECT_NAME}}", project_name).replace(
                "{{SCAFFOLD_DATE}}", scaffold_date
            )
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new platform repo from the foundation template.")
    parser.add_argument("--name", required=True, help="Project name (used for folder name and placeholders)")
    parser.add_argument("--target", required=True, help="Parent directory to create the new project folder in")
    args = parser.parse_args()

    if not TEMPLATE_DIR.exists():
        print(f"❌ Template not found at {TEMPLATE_DIR}. Is this script running from within the skill folder?")
        sys.exit(1)

    target_parent = Path(args.target).expanduser().resolve()
    if not target_parent.exists():
        print(f"❌ Target parent directory does not exist: {target_parent}")
        sys.exit(1)

    project_dir = target_parent / args.name
    if project_dir.exists():
        print(f"❌ {project_dir} already exists — refusing to overwrite. Remove it or pick a different name.")
        sys.exit(1)

    print(f"Copying template → {project_dir}")
    shutil.copytree(TEMPLATE_DIR, project_dir)

    print("Replacing placeholders...")
    replace_placeholders(project_dir, args.name, date.today().isoformat())

    print(f"✅ Scaffolded '{args.name}' at {project_dir}")
    print("")
    print("Next steps:")
    print(f"  cd {project_dir}")
    print("  git init && git add . && git commit -m 'Initial scaffold from repo-foundation'")
    print("  # Fill in ARCHITECTURE.md and README.md with real project details")
    print("  # Create the GitHub repo under LuaAccess org, then git push")
    print("  # Confirm render.yaml's disk path and Node version before first deploy")
    print("  # Walk CHECKLIST.md before going live")


if __name__ == "__main__":
    main()
