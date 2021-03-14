#!/usr/bin/env python3

import matplotlib.pyplot as plt
import base64
import io
def save(path):
    f = io.BytesIO()
    cnt = 0
    with open(path, "w") as file:
        for num in plt.get_fignums():
            f.seek(0)
            plt.figure(num).savefig(f)
            f.seek(0)
            s = base64.b64encode(f.read()).decode()
            file.write('<img src="data:image/png;base64,%s"/>\n' % s)
            cnt += 1
            if cnt % 2 == 0:
                file.write("</br>\n")
    return cnt

plt.figure()
plt.plot([1, 2, 3, 4, 5], 'r-')

plt.figure()
plt.plot([10, 2, 30, 4, 50], 'b-')

plt.figure()
plt.plot([10, 2, 30, 4, 50], 'g-')

plt.figure()
plt.plot([10, 2, 12, 6, 50], 'm-')

print(save("a.md"))
