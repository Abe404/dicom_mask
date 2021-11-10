# dicom_mask
Export structure from dicom to numpy binary mask

### Install

> pip install dicom-mask

### Example usage

```python
from dicom_mask.convert import struct_to_mask

dicom_dir = 'some_dicom_dir'
dicom_files = ['all', 'image', 'filenames', 'and', 'struct']
struct_name = 'liver' 

mask = struct_to_mask(dicom_dir, dicom_files, struct_name)
```


## Citation

If you find this module useful in your research, please cite the following paper:

"Gating has a negligible impact on delivered dose in 20 patients treated with MRI-guided online adaptive radiotherapy for prostate cancer"

Where it is described and for which it was initially developed.
