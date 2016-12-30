## The Gauss-Legendre Algorithm

The Gauss-Legendre algorithm is a quadratically convergant method of compiting pi.  It can be expressed mathematically as an infinite sequence of approximations:

![setup](https://wikimedia.org/api/rest_v1/media/math/render/svg/07cb5ca2a99df7d66078e7f2d626b9fd6e0ec839)

![iteration](https://wikimedia.org/api/rest_v1/media/math/render/svg/000357c43f0f911092d9e5129dcc45227565bcf8)

![pi](https://wikimedia.org/api/rest_v1/media/math/render/svg/70561e8aed278793d403e309309151199a765fd1)

which can be converted to psudocode:
```
a0 = 1
b = 1/sqrt(2)
t = 1/4
p = 1
repeat as needed {
	a1 = (a0 + b) / 2
	b = sqrt(a0 * b)
	t = t - p * sqr(a0 - a1)
	a0 = a1
	p = p * 2
}
pi = sqr(a + b) / (4 * t)
```

where `sqrt` and `sqr` are the square root and the square functions.  Note that two 'versions' of `a` are needed for updating `t`.

This repo contains both a Python and C implementation of the above psudocode.