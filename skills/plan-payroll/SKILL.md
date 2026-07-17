---
name: plan-payroll
description: Plan and structure payroll runs — headcount cost modeling, statutory deduction estimates, payroll calendar sequencing, and variance flagging between planned and actual payroll cost. Use when planning next period's payroll budget, modeling the cost of a new hire or raise, sequencing a payroll calendar and cutoff dates, or reconciling planned vs. actual payroll spend. Triggers include "plan payroll", "payroll budget", "cost of hiring", "payroll calendar", "payroll cutoff", "13th month", "statutory deductions estimate". Does NOT compute or file actual statutory remittances (SSS, PhilHealth, Pag-IBIG, BIR withholding) — those figures must be verified against current official tables/rates before use; this skill produces planning estimates only, not filing-ready numbers. Does NOT cover individual employee compensation benchmarking or offer negotiation — see human-resources:comp-analysis or human-resources:draft-offer. Does NOT cover journal entries for payroll — see finance:journal-entry-prep.
---

# Plan Payroll

## Purpose
Model payroll cost and timing before it happens — so budget surprises (a new hire's real fully-loaded cost, an upcoming 13th-month liability, a cutoff that lands on a holiday) get caught in planning, not in the close.

## Gotchas
- **This is a planning tool, not a filing tool.** Never present SSS/PhilHealth/Pag-IBIG/BIR contribution figures as filing-ready. Official rates change (contribution tables have been revised multiple times in recent years) — always state the estimate is based on rates as of a stated date and flag it needs verification against current BIR/SSS/PhilHealth/Pag-IBIG tables before actual filing.
- **Fully-loaded cost ≠ base salary.** A new hire's real monthly cost includes employer-side statutory contributions, mandated benefits (13th month accrual, if applicable de minimis benefits), and often a recruitment/onboarding amortized cost. Quoting base salary alone as "the cost" undersells the budget impact — always show both.
- **13th month is a liability that accrues monthly, not a December surprise.** When planning annual payroll budget, always show the 1/12 monthly accrual, not just a December lump sum, so cash flow planning isn't caught off guard.
- **Cutoff dates shift around Philippine holidays.** When sequencing a payroll calendar, cross-check pay dates against the official PH holiday list for that year — a cutoff landing on a non-working day needs to move, and this affects both bank processing and DOLE-mandated final pay timing for any offboarding in the same period.
- **Don't conflate contractor/manpower-agency costs with direct payroll.** If any headcount is agency-supplied (relevant given manpower/staffing account context), their cost model is markup-on-billing, not payroll deductions — keep these separate in any report.

## Workflow
1. Clarify scope: new hire cost model, full-period payroll budget, calendar sequencing, or variance check (planned vs. actual).
2. For cost modeling: base salary + estimated employer-side statutory contributions (stated as estimates, dated) + 13th-month monthly accrual + any known fixed benefits.
3. For calendar sequencing: lay out cutoff → processing → pay date per cycle, cross-referenced against PH holidays; flag any cutoff needing to shift.
4. For variance: compare planned vs. actual, flag any variance above a materiality threshold (ask user if none given, default 5%), and identify likely driver (headcount change, overtime, late hire/exit, contribution rate change).
5. Always close with an explicit verification flag: "Contribution estimates based on rates as of [date] — confirm against current SSS/PhilHealth/Pag-IBIG/BIR tables before finalizing actual payroll."

## Output
- Structured table: base cost, statutory estimate (flagged), accruals, total fully-loaded estimate
- Payroll calendar (if requested) with cutoff/process/pay date columns
- One-line verification flag (mandatory, every output)
- Handoff note if actual filing, DOLE compliance question, or contractor/agency billing dispute is involved — those go to a licensed payroll processor or `human-resources` bundle, not this skill
