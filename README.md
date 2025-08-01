# Thoughtful test project to apply for Staff Data Engineer role

# Package Type Sorter

A simple Python utility to determine package type (`NORMAL`, `SPECIAL`, or `REJECTED`) based on the dimensions and mass of the package.

---

## 📦 Description

This script uses a set of conditional rules to evaluate whether a package is:
- **NORMAL**: Small in volume and light in mass.
- **SPECIAL**: Either large in volume or heavy, but within allowable limits.
- **REJECTED**: Too large or too heavy to be accepted.

It prints debug information to help visualize which rule path was taken.

---

## 🧠 Logic Summary

- If all dimensions (`width`, `height`, `length`) are under 150:
  - Calculate volume = width × height × length
  - If volume < 1,000,000 and mass < 20 → `NORMAL`
  - If either volume ≥ 1,000,000 or mass ≥ 20 → `SPECIAL`
  - If both volume ≥ 1,000,000 and mass ≥ 20 → `REJECTED`

- If any dimension ≥ 150:
  - If mass < 20 → `SPECIAL`
  - Else → `REJECTED`

---

## 🧪 Sample Output

```python
print(sort(20, 130, 130, 19))   # Output: NORMAL
print(sort(120, 130, 130, 19))  # Output: SPECIAL
print(sort(120, 130, 130, 20))  # Output: REJECTED
print(sort(20, 130, 150, 19))   # Output: SPECIAL
print(sort(20, 130, 150, 20))   # Output: REJECTED
