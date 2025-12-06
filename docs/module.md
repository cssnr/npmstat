---
icon: fontawesome/brands/python
---

# :fontawesome-brands-python: Python Module

You can import the methods directly.

```python
from npmstat import api

r = api.get_package('package')
print(f'cached: {r.from_cache}')
print(r.json())


api.session.cache.clear()
print('cache cleared')
```

For more details see the [api.py](https://github.com/cssnr/npmstat/blob/master/src/npmstat/api.py) source code.

!!! warning

    This API is incomplete and expected to change in the future.

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
