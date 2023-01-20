# Exercise7.20
import random
import numpy as np
%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 1)]
%timeit rolls_array = np.random.randint(1, 7, 1)

%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 10)]
%timeit rolls_array = np.random.randint(1, 7, 10)

%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 100)]
%timeit rolls_array = np.random.randint(1, 7, 100)

%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 1000)]
%timeit rolls_array = np.random.randint(1, 7, 1000)

%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 10_000)]
%timeit rolls_array = np.random.randint(1, 7, 10_000)

%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 100_000)]
%timeit rolls_array = np.random.randint(1, 7, 100_000)

%timeit rolls_list = [random.randrange(1, 7) for i in range(0, 1_000_000)]
%timeit rolls_array = np.random.randint(1, 7, 1_000_000)


import pandas as pd
number=[1,10,100,1000,10_000,100_000,1_000_000]

list_ave=['776 ns ± 7.64 ns','5.23 µs ± 139 ns','48.8 µs ± 576 ns','487 µs ± 2.51 µs','5.02 ms ± 95.4 µs','49.7 ms ± 998 µs','507 ms ± 9.47 ms']
array_ave=['5.76 µs ± 49.5 ns','5.85 µs ± 234 ns','6.45 µs ± 65.3 ns','12.7 µs ± 198 ns','71.4 µs ± 656 ns','659 µs ± 5.52 µs','7.09 ms ± 25.7 µs']
print(pd.DataFrame({'Number_of_values':number, 'List_ave_time':list_ave, 'Array_ave_time':array_ave}))