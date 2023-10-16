# FastParquet issue reproduction repo

Code snippets and data files for reporting FastParquet issues of reading Parquet files.

- Uses [Poetry](https://python-poetry.org/docs/#installation) to install packages
- Uses [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) to handle files (500MB+)

Usage:

```shell
git clone git@github.com:tradingstrategy-ai/fastparquet-reproduction.git
cd fastparquet-reproduction
git lfs install
git lfs pull
poetry install
peotry shell
python fastparquet-decompression-error.py
```

Will give you:

```
Traceback (most recent call last):
  File "/Users/moo/code/ts/fastparquet-bugsies/fastparquet-decompression-error.py", line 23, in <module>
    df2 = pf2.to_pandas()
          ^^^^^^^^^^^^^^^
  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/api.py", line 784, in to_pandas
    self.read_row_group_file(rg, columns, categories, index,
  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/api.py", line 386, in read_row_group_file
    core.read_row_group(
  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/core.py", line 632, in read_row_group
    read_row_group_arrays(file, rg, columns, categories, schema_helper,
  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/core.py", line 602, in read_row_group_arrays
    read_col(column, schema_helper, file, use_cat=name+'-catdef' in out,
  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/core.py", line 497, in read_col
    num += read_data_page_v2(infile, schema_helper, se, ph.data_page_header_v2, cmd,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/moo/Library/Caches/pypoetry/virtualenvs/fastparquet-bugsies-qrDtU46f-py3.11/lib/python3.11/site-packages/fastparquet/core.py", line 290, in read_data_page_v2
    decomp(np.frombuffer(infile.read(size), dtype="uint8"),
cramjam.DecompressionError: snappy: output buffer (size = 262144) is smaller than required (size = 1048576)
```