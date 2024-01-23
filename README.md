# Global FWI utils

Some of the LASIF functionalities are becoming more and more difficult to maintain. Therefore, it makes sense to move some of the utilities, like plotting-functions, outside of LASIF. This repository runs with minimal requirements.

Set up a new conda - environment.

```
conda env create -f environment.yml
```

```
conda activate lasif-utils 
```

And we are ready to go.

# Contributions

Whenever you write a new plotting routine or refine one of existing ones, please consider commiting it to this repo. There is no need to re-invent the wheel again and again.

# Functionalities

In general, it's advised to copy the notebooks and scripts to a place outside of the

## Extract source and receivers

`/notebooks/extract_source_and_receivers.py`

This function runs through all of your Event-files in your data projects and creates a list of coordinates with all source-receiver pairs. The list is essential for plotting routines like ray-density and source-receiver geometries and allows to use these functions outside of LASIF. Can be run on daint itself when the data is stored remotely.

Before use
- Check the savepath
- Check the path to the DATA repo