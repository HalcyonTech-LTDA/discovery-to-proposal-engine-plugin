#!/usr/bin/env python3
"""
Automated Validator for Pre-Proposal Technical Dossiers (DOSSIE_TECNICO_PRE_PROPOSTA.md)
Ensures full compliance with the 8 mandatory chapters, strict anti-slide enforcement,
anti-hallucination indicators, required analytical depth, and tabular data integrity.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

# 8 Mandatory Chapters (Pattern matching supporting EN and PT headings)
MANDATORY_CHAPTERS: List[Tuple[int, str, List[str]]] = [
    (1, "Executive Summary & Problem Statement", [
        r"(#+\s*(1\.?\s*)?Resumo\s+Executivo\s+do\s+Problema|#+\s*(1\.?\s*)?Executive\s+Summary\s+of\s+Problem)",
    ]),
    (2, "Delimitation Matrix: In-Scope vs Explicit Out-of-Scope", [
        r"(#+\s*(2\.?\s*)?Matriz\s+de\s+Delimita[çc][ãa]o.*Escopo|#+\s*(2\.?\s*)?Delimitation\s+Matrix.*Scope)",
    ]),
    (3, "Macro Architecture, Critical Integrations & Technical Red Flags", [
        r"(#+\s*(3\.?\s*)?Relat[óo]rio\s+de\s+Arquitetura\s+Macro|#+\s*(3\.?\s*)?Macro\s+Architecture.*Red\s+Flags)",
    ]),
    (4, "Decomposition into Macro-Epics & Analogy Estimation (T-Shirt Sizing)", [
        r"(#+\s*(4\.?\s*)?Decomposi[çc][ãa]o\s+em\s+Macro-[ÉE]picos|#+\s*(4\.?\s*)?Macro-Epic\s+Decomposition.*T-Shirt)",
    ]),
    (5, "Staffing Plan & Squad Topology (75-80% Utilization)", [
        r"(#+\s*(5\.?\s*)?Plano\s+de\s+Staffing|#+\s*(5\.?\s*)?Staffing\s+Plan.*Squad)",
    ]),
    (6, "Macro Schedule by Delivery Milestones (M0 - M4)", [
        r"(#+\s*(6\.?\s*)?Cronograma\s+Macro\s+por\s+Marcos|#+\s*(6\.?\s*)?Macro\s+Schedule.*Milestones)",
    ]),
    (7, "Governance Guidelines, UAT/Homologation & Tacit Acceptance", [
        r"(#+\s*(7\.?\s*)?Diretrizes\s+de\s+Governan[çc]a.*Homologa[çc][ãa]o|#+\s*(7\.?\s*)?Governance\s+Guidelines.*Acceptance)",
    ]),
    (8, "Commercial Model Recommendation & Pricing Support Memory", [
        r"(#+\s*(8\.?\s*)?Recomenda[çc][ãa]o\s+de\s+Modelo\s+Comercial|#+\s*(8\.?\s*)?Commercial\s+Model\s+Recommendation)",
    ]),
]

# Forbidden Slide & Pitch Deck Markers
FORBIDDEN_SLIDE_PATTERNS: List[str] = [
    r"^\s*Slide\s+\d+[:\-]",
    r"^\s*\[Slide\s+\d+\]",
    r"^\s*#+\s*Slide\s+\d+",
    r"Pitch\s+Deck\s+Outline",
    r"Slide\s+Title:",
    r"Deck\s+Presentation",
    r"Bullet\s+Slide",
]

# Mandatory Substantive Checks
MANDATORY_CONCEPTS: List[Tuple[str, List[str]]] = [
    ("Delimitation Matrix Table", [r"\|\s*.*In-Scope.*\|\s*.*Out-of-Scope.*\||\|\s*.*Escopo Contemplado.*\|\s*.*N[ãa]o-Escopo.*\|"]),
    ("Technical Red Flags Analysis", [r"Red\s*Flag|TRF-\d+|Risco\s+T[ée]cnico"]),
    ("Phase 0 (Inception) Formal Verdict", [r"Fase\s+0|Phase\s+0|Inception\s+T[ée]cnica|Technical\s+Inception"]),
    ("T-Shirt Sizing Application", [r"(T-Shirt|Tamanho\s+de\s+Camiseta).*(S|M|L|XL|P|M|G|GG)"]),
    ("Utilization Factor (75-80%)", [r"75\s*%\s*a\s*80\s*%|75%-80%|80%\s*utiliz|fator\s+de\s+utiliza[çc][ãa]o"]),
    ("Delivery Milestones (M0 to M4)", [r"M0.*Inception|M1.*Core|M2.*Integra|M3.*(UAT|Homologa)|M4.*(Go-Live|Cutover)"]),
    ("Tacit Acceptance Clause (Aceite Tácito)", [r"[Aa]ceite\s+[Tt][áa]cito|[Tt]acit\s+[Aa]cceptance"]),
    ("5 Business Days Homologation SLA", [r"5\s*(?:\([cC]inco\)\s*)?dias\s+[úu]teis|5\s*business\s*days|\b5\s*dias\s+[úu]teis\b"]),
    ("Change Request (CR) Protocol", [r"Change\s+Request|CR\b|Gest[ãa]o\s+de\s+Mudan[çc]as"]),
]


def audit_dossier(filepath: str) -> bool:
    path = Path(filepath)
    if not path.exists():
        print(f"❌ ERROR: File does not exist: {filepath}")
        return False

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    word_count = len(re.findall(r"\w+", content))

    print("=================================================================")
    print("🔍 AUDITING PRE-PROPOSAL TECHNICAL DOSSIER")
    print(f"📄 File: {filepath}")
    print(f"📊 Total Lines: {len(lines)} | Total Words: {word_count}")
    print("=================================================================\n")

    passed = True

    # 1. Minimum Density Check
    if word_count < 1200:
        print(f"❌ FAIL: Insufficient analytical density ({word_count} words). Minimum required is 1,200 words.")
        passed = False
    else:
        print(f"✅ PASS: Analytical density verified ({word_count} words).")

    # 2. Strict Anti-Slide Verification
    slide_violations = []
    for idx, line in enumerate(lines, 1):
        for pattern in FORBIDDEN_SLIDE_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                slide_violations.append((idx, line.strip(), pattern))

    if slide_violations:
        print("❌ FAIL: FORBIDDEN SLIDE PATTERNS DETECTED!")
        for line_no, text, pattern in slide_violations:
            print(f"   Line {line_no}: '{text}' matched forbidden pattern '{pattern}'")
        passed = False
    else:
        print("✅ PASS: Strict Anti-Slide verification passed (0 slide/deck markers found).")

    # 3. Mandatory 8 Chapters Verification
    print("\n--- Auditing 8 Mandatory Chapters ---")
    for chapter_num, chapter_title, patterns in MANDATORY_CHAPTERS:
        found = False
        for p in patterns:
            if re.search(p, content, re.IGNORECASE):
                found = True
                break
        if found:
            print(f"✅ Chapter {chapter_num}: {chapter_title} present.")
        else:
            print(f"❌ FAIL: Missing Chapter {chapter_num}: {chapter_title}")
            passed = False

    # 4. Mandatory Substantive Concepts & Tables
    print("\n--- Auditing Mandatory Technical & Governance Safeguards ---")
    for concept_name, patterns in MANDATORY_CONCEPTS:
        found = any(re.search(p, content, re.IGNORECASE) for p in patterns)
        if found:
            print(f"✅ Concept verified: {concept_name}")
        else:
            print(f"❌ FAIL: Missing mandatory concept: {concept_name}")
            passed = False

    # 5. Macro-Epic Count Check (Must have 5 to 8 epics)
    epic_matches = re.findall(r"(?:EPIC|ÉPICO|Épico|Epic)[-\s_]*0?([1-9])", content, re.IGNORECASE)
    unique_epics = set(epic_matches)
    if len(unique_epics) < 5:
        print(f"⚠️ WARNING: Found only {len(unique_epics)} distinct macro-epics. Minimum recommended is 5 to 8.")
    else:
        print(f"✅ Epic Count verified: {len(unique_epics)} distinct macro-epics detected.")

    print("\n=================================================================")
    if passed:
        print("🎯 FINAL VERDICT: PASS! All pre-sales engineering guardrails verified.")
        print("=================================================================")
        return True
    else:
        print("💥 FINAL VERDICT: FAIL! Dossier does not meet all mandatory standards.")
        print("=================================================================")
        return False


def main():
    parser = argparse.ArgumentParser(description="Audit and validate pre-proposal technical dossiers.")
    parser.add_argument("file", help="Path to DOSSIE_TECNICO_PRE_PROPOSTA.md")
    args = parser.parse_args()

    success = audit_dossier(args.file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
