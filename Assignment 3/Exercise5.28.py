#Exercise 5.28
import numpy as np
import statistics as stats
scale=[1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
quality,count=np.unique(scale,return_counts=True)
quality=list(quality)
count=list(count)
for q,c in zip(quality, count):
    print(f'{q}  {c}')

print(f'Min is {quality[count.index(min(count))]};frequency:{min(count)}')
print(f'Max is {quality[count.index(max(count))]};frequency:{max(count)}')
print(f'Range:from {min(count)} to {max(count)}')
print('Median:',stats.median(count))
print('Mean:',stats.mean(count))
print('Mode:',stats.mode(count))
print('Variance:',stats.variance(count))
print('Standard deviation:',stats.pstdev(count))
