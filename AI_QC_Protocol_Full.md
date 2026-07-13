# Human + AI Quality Control Protocol for Analytical Code

## Purpose

This document presents a structured quality control protocol for analytical coding workflows in environments where human analysts use AI tools to accelerate code development, review, and validation. The protocol is designed to make analytical outputs more reliable, auditable, and scientifically defensible, with relevance to data-intensive domains such as life cycle assessment, sustainability analysis, and other quantitative decision-support workflows.

## Executive Summary

AI can substantially improve the speed of analytical coding, but it also introduces new quality risks when generated code is accepted without sufficient review.

This protocol establishes a human-led, AI-assisted approach to quality control. It separates responsibilities across setup, review, critique, execution, testing, validation, and standardization so that analysts can benefit from AI productivity while maintaining accountability for data integrity and scientific interpretation.

> Use AI to surface assumptions, identify failure modes, generate tests, and strengthen validation logic, but rely on human judgment to define the analytical objective, assess scientific plausibility, and approve results.

\---

## Key Concepts

### Human Accountability

The analyst remains responsible for the correctness, relevance, and defensibility of the workflow.

### Data Integrity

Analytical code must preserve the intended meaning of the dataset.

### Invariants

Conditions that should remain true before and after transformation:

* Row counts
* Unique identifiers
* Totals
* Categories
* Expected value ranges

### Adversarial Review

Use AI to challenge assumptions, identify edge cases, and expose silent failure modes.

\---

## Core Principles

* Human accountability remains primary.
* Code correctness alone is insufficient.
* Every transformation should have validation evidence.
* High-risk operations require additional scrutiny.
* QC should be repeatable, documented, and standardized.

# Phase 0: Defensive Setup

## How to Apply

1. State the analytical question.
2. Identify inputs, outputs, and decision context.
3. Define invariants.
4. Identify high-risk operations.

### Recommended AI Prompt

```text
Write Python code that enforces the following constraints: preserve row count, ensure one-to-one mapping, raise errors for duplicates or missing values, and output validation summaries.
```

# Phase 1: First-Pass Human Review

1. Read workflow from input to output.
2. Verify alignment with objective.
3. Review merges, joins, filters, groupby operations, unit conversions, and imputations.
4. Confirm validations exist.
5. Ensure readability and auditability.

# Phase 2: AI-Assisted Critique

1. Provide code and objective.
2. Identify assumptions.
3. Identify silent failures.
4. Generate tests and assertions.
5. Manually review recommendations.

### Prompts

* What assumptions does this code make?
* List realistic silent failure scenarios.
* Could this duplicate rows, drop data, or introduce nulls?
* Add assertions for row counts and uniqueness.

# Phase 3: Controlled Execution

1. Run incrementally.
2. Capture row counts.
3. Inspect nulls, duplicates, unmatched records, categories.
4. Review representative samples.
5. Store diagnostics.

# Phase 4: Adversarial Testing

Test:

* Duplicate keys
* Missing values
* Unexpected categories
* Negative quantities
* Unit mismatches
* Empty datasets

# Phase 5: Final Human Validation

1. Compare with expectations and benchmarks.
2. Verify invariants.
3. Review warnings and exclusions.
4. Document acceptance rationale.
5. Ensure explainability.

> This phase cannot be delegated to AI.

# Phase 6: QA Standardization

1. Reusable validation functions.
2. Shared QA libraries.
3. Diagnostic logging.
4. Stored test cases.
5. Continuous improvement.

## Defensive Coding Patterns

* Assert key uniqueness.
* Verify row counts.
* Check null values.
* Report unmatched records.
* Log intermediate summaries.
* Validate units and ranges.
* Use clear error messages.

## Conclusion

The most reliable approach combines human accountability with structured AI critique and repeatable validation.

## References and Suggested Reading

### AI-Assisted Coding

* Factors Influencing the Quality of AI-Generated Code: A Synthesis of Empirical Evidence
* Automating Code Review: A Systematic Literature Review
* Human-AI Experience in Integrated Development Environments
* Human-in-the-Loop Artificial Intelligence

### Software Testing

* LLMLOOP
* Artificial Intelligence in Software Testing

### Reproducible Workflows

* Principles for Data Analysis Workflows
* Reproducible Machine Learning-Enabled Workflow
* Applying FAIR Principles to Computational Workflows

### Data Quality

* Great Expectations (GX Core)
* Pandera
* Data Quality as Code

### Life Cycle Assessment

* Life Cycle Assessment under Uncertainty
* Data Quality in openLCA
* Comparative Study of Standardised Inputs and Inconsistent Outputs in LCA Software

