# 🐍 Python Quick Information

> Roz 5 minute dekho — 2 hafte me yaad ho jayega

---

## 1. Basic Types — One Line Summary

| Type | Example | Mutable | Ordered | Dup | Rule |
|------|---------|:-------:|:-------:|:---:|------|
| `int` | `5` | ❌ | — | — | Whole number |
| `float` | `3.14` | ❌ | — | — | Decimal number |
| `bool` | `True/False` | ❌ | — | — | Only 2 values |
| `str` | `'hello'` | ❌ | ✅ | ✅ | **Immutable** — cannot change |
| `list` | `[1,2,3]` | ✅ | ✅ | ✅ | `[ ]` changeable |
| `tuple` | `(1,2,3)` | ❌ | ✅ | ✅ | `( )` locked list |
| `set` | `{1,2,3}` | ✅ | ❌ | ❌ | `{ }` no colon, no dup |
| `dict` | `{'a':1}` | ✅ | ✅ | keys | `{key:value}` |
| `None` | `None` | ❌ | — | — | Nothing value |

---

## 2. Mutable vs Immutable

- ✅ **Mutable** (change ho sakta): `list`, `set`, `dict`
- ❌ **Immutable** (change NAHI hota): `int`, `float`, `str`, `tuple`, `bool`, `None`

```python
# string immutable
s = "hello"
s[0] = "H"      # ❌ TypeError
s = "Hello"     # ✅ naya string

# list mutable
lst = [1, 2, 3]
lst[0] = 99     # ✅ [99, 2, 3]
