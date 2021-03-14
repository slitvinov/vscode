#!/usr/bin/env python3

import matplotlib.pyplot as plt
from base64 import b64encode
import io

f = io.BytesIO()
plt.plot([1, 2, 3, 4, 5], 'o-')
plt.savefig(f)

f.seek(0)
s = b64encode(f.read()).decode()
with open("a.md", "w") as f:
    f.write('<img src="data:image/png;base64,%s"/>' % s)
