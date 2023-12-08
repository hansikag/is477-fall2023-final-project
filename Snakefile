rule prepare:
    input:
        script="scripts/prepare_data.py"
    output:
        "data/dataset.zip"
    run:
        shell("python {input.script}")

rule profile:
    input:
        script="scripts/profile.py",
        dataset="data/wine.data"
    output:
        "profiling/report.html"
    run:
        shell("python {input.script}")

rule analyze:
    input:
        script="scripts/analysis.py",
        dataset="data/wine.data"
    output:
        "results/"
    run:
        shell("python {input.script}")
