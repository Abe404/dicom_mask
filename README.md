# dicom-mask

Export structure from dicom to numpy binary mask

### Why does this exist?

Dicom-mask was developed by the radiation-oncology research group at Rigshospitalet, Denmark.

We implemented dicom-mask because the existing DICOM export tools we found failed to extract the DICOM RTSTRUCT (1) information from our ViewRay DICOM files. dicom-mask contains code modified from dicompyler (2) and uses dicompyler-core (3) and scikit-image (4) to extract RTSTRUCT data into a NumPy (5) ndarray object. 


### Install

The latest version is available via PyPI (https://pypi.org/project/dicom-mask) for convenient installation with pip

> pip install dicom-mask

### Example usage

```python
from dicom_mask.convert import struct_to_mask

dicom_dir = 'some_dicom_dir'
dicom_files = ['all', 'dicom', 'series', 'image', 'filenames', 'and', 'struct', 'filename']
struct_name = 'liver' 

mask = struct_to_mask(dicom_dir, dicom_files, struct_name)
```

## Citation


The paper for which it was initially developed is:

"Gating has a negligible impact on the dose delivered to 20 prostate cancer patients treated with MRI-guided online adaptive radiotherapy"

For citation of the tool please cite the [zenodo repository](https://zenodo.org/record/5727328)

Abraham George Smith. (2021). Abe404/dicom_mask: 0.0.17b (0.0.17b). Zenodo. https://zenodo.org/record/5727328

### References 

1. Gorthi, Subrahmanyam & Bach Cuadra, Meritxell & Thiran, Jean-Philippe. (2009). Exporting Contours to DICOM-RT Structure Set.
2. Panchal, Aditya, and Roy Keyes. "SU‐GG‐T‐260: dicompyler: an open source radiation therapy research platform with a plugin architecture." Medical Physics 37.6Part19 (2010): 3245-3245.
3. Aditya Panchal, pyup.io bot, Gabriel Couture, gertsikkema, Nicolas Galler, Hideki_Nakamoto, David C Hall, & Akihisa Wakita. (2019). dicompyler/dicompyler-core v0.5.5 (v0.5.5). Zenodo. https://doi.org/10.5281/zenodo.3236628
4. Stéfan van der Walt, Johannes L. Schönberger, Juan Nunez-Iglesias, François Boulogne, Joshua D. Warner, Neil Yager, Emmanuelle Gouillart, Tony Yu and the scikit-image contributors. scikit-image: Image processing in Python. PeerJ 2:e453 (2014) https://doi.org/10.7717/peerj.453
5. Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).
