import pandas as pd
import pandera as pa
from recap.schema.converters.pandera import from_pandera
import numpy as np

df = pd.DataFrame({
    'null_col': [None]*5,
    'bool_col': [True, False, True, False, True],
    # 'uint8_col': np.random.randint(low=0, high=255, size=5, dtype=np.uint8),
    'int8_col': np.random.randint(low=-128, high=127, size=5, dtype=np.int8),
    # 'uint16_col': np.random.randint(low=0, high=65535, size=5, dtype=np.uint16),
    'int16_col': np.random.randint(low=-32768, high=32767, size=5, dtype=np.int16),
    # 'uint32_col': np.random.randint(low=0, high=4294967295, size=5, dtype=np.uint32),
    'int32_col': np.random.randint(low=-2147483648, high=2147483647, size=5, dtype=np.int32),
    # 'uint64_col': np.random.randint(low=0, high=18446744073709551615, size=5, dtype=np.uint64),
    'int64_col': np.random.randint(low=-9223372036854775808, high=9223372036854775807, size=5, dtype=np.int64),
    # 'float16_col': np.random.randn(5).astype(np.float16),
    'float32_col': np.random.randn(5).astype(np.float32),
    'float64_col': np.random.randn(5).astype(np.float64),
    'time_col': pd.to_datetime(['2022-01-01 00:00:00', '2022-01-01 01:00:00', '2022-01-01 02:00:00', '2022-01-01 03:00:00', '2022-01-01 04:00:00']),
    'date_col': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']).date,
    'timestamp_col': pd.Timestamp.now(),
    'duration_col': pd.to_timedelta(np.random.randint(low=0, high=1000, size=5), unit='ms'),
    'bytes_col': [b'hello', b'world', b'python', b'data', b'science'],
    'string_col': ['apple', 'banana', 'cherry', 'dates', 'elderberry'],
    'decimal_col': [0.1, 0.2, 0.3, 0.4, 0.5],
    'map_col': [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}, {'e': 5}],
    'struct_col': [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}, {'g': 7, 'h': 8}, {'i': 9, 'j': 10}],
    'field_col': ['a', 'b', 'c', 'd', 'e'],
    'array_col': [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
})

pandera_schema = pa.infer_schema(df)
print(pandera_schema)
recap_schema = from_pandera(pandera_schema)
print(recap_schema)

import ipdb; ipdb.set_trace()
