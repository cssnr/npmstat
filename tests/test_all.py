from npmstat import api


def test_info():
    r = api.get_package("@cssnr/vitepress-swiper", "0.0.1")
    print(f"{r.status_code=}")
    print(f"{r.from_cache=}")
    assert r.status_code == 200
    assert r.json()


def test_stats():
    r = api.get_downloads("@cssnr/vitepress-swiper")
    print(f"{r.status_code=}")
    print(f"{r.from_cache=}")
    assert r.status_code == 200
    assert r.json()
