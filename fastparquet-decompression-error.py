"""Compare pyarrow and fastparquet files.

- Use the sample Parquet file (54MB): https://drive.google.com/file/d/1LtiL-n50cNx1JMBC0QE-Ztvf8ENSb-OE/view?usp=sharing
  - save as "/tmp/candles-30d.parquet"

- We found out that rows and the contents of pair_id column is corrupted
  (among other corruption if you do row by row comparison, but this is easy to spot)]

- One potential cause is usage of row groups in the file

- The file has been written with pyarrow / Python


"""
from pyarrow import parquet as pq  # pyarrow 10
from fastparquet import ParquetFile  # fastparquet  2023.1.0

path = "./lending-reserves-all.parquet"

df1 = pq.read_table(path).to_pandas()

pf2 = ParquetFile(path)

# Will bomb out
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/core.py", line 290, in read_data_page_v2
#    decomp(np.frombuffer(infile.read(size), dtype="uint8"),
# cramjam.DecompressionError: snappy: output buffer (size = 262144) is smaller than required (size = 1048576)

df2 = pf2.to_pandas()

