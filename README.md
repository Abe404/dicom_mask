# dicom_mask
Export structure from dicom to numpy binary mask

### Install

> pip install dicom-mask

### Examle usage

```python
from dicom_mask.convert import struct_to_mask

dicom_dir = 'some_dicom_dir'
dicom_files = ['all', 'image', 'filenames', 'and', 'struct']
struct_name = 'liver' 

mask = struct_to_mask(dicom_dir, dicom_files, struct_name)
```
