---
icon: fontawesome/brands/python
---

# :fontawesome-brands-python: Python Module

You can import the module directly.

```python
import npmstat

r = npmstat.get_package("@cssnr/vitepress-swiper")
print(f"{r.from_cache=}")
print(r.json())
```

Or import the api directly.

```python
from npmstat import api

r = api.get_downloads("@cssnr/vitepress-swiper", "last-week")
print(f"{r.from_cache=}")
print(r.json())

api.session.cache.clear()
print("cache cleared")
```

For more details see the [api.py :lucide-arrow-up-right:](https://github.com/cssnr/npmstat/blob/master/src/npmstat/api.py) source code.

!!! warning "This API is incomplete and may change in the future."

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
