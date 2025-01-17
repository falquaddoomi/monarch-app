import pytest


@pytest.fixture
def association_counts():
    return {
        "items": [
            {"label": "Phenotypes", "count": 4027, "category": "biolink:DiseaseToPhenotypicFeatureAssociation"},
            {"label": "Causal Genes", "count": 124, "category": "biolink:CausalGeneToDiseaseAssociation"},
            {"label": "Correlated Genes", "count": 151, "category": "biolink:CorrelatedGeneToDiseaseAssociation"},
        ]
    }
