rule prepare:
    output:
        "data/wine.data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/wine.data"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    input: 
        "data/wine.data"
    output:
        "results/"
    shell:
        "python scripts/analysis.py"
