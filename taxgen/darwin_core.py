# Mappings from iNaturalist metadata to DarwinCore properties
# Update: Just discovered this:
# https://github.com/inaturalist/inaturalist/tree/3c9b2daa61d97de0d50083f3c5c72cf2ed210397/lib/darwin_core
# TODO: Replicate iNat's existing mappings (for dwc archives), but for XMP

INAT_DWC_ATTRIBUTE_MAP = {
    'taxon_id': 'taxonID',
    'observation_id': 'occurrenceID',  # Or catalogNumber?
    'common_name': 'vernacularName',   # Use comma-delimited list?
    'life_stage': 'lifeStage',
    'username': 'recordedBy',
    'description': 'fieldNotes',
    # Primary ranks mostly map 1:1
    'kingdom': 'Kingdom',
    'phylum': 'Phylum',
    'class': 'Class',
    'order': 'Order',
    'family': 'Family',
    'genus': 'Genus',
    'subgenus': 'Subgenus',
    'species': 'Species',
    'binomial': 'scientificName',
    # '???': 'specificEpithet',
    # '???': 'taxonRank',                # Most specific rank according to community ID
    # '???': 'institutionCode',          # Populate this with 'iNaturalist'?
    # '???': 'associatedOccurrences'     # Link other iNat observations of the same taxon?
    #  '???': 'higherClassification',
    # dwc doesn't seem to have attributes for intermediate ranks (superfamily, etc.)
    #     ...except subgenus, apparently?
    #     Maybe use higherClassification property?
    # Are the dwc geospatial properties needed, or redundant with other GPS XMP/EXIF metadata?
    # Could use other properties in dwc:Occurrence struct for more observation details
    # Additional properties might map to existing observation fields (interactions, behavior, etc.)
}
