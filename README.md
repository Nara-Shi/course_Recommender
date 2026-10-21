# Course Recommender

A small Streamlit prototype that recommends sample courses from a learner's selected topics, current level, and preferred maximum duration.

## How it works

- Select one or more interests.
- Filter by beginner, intermediate, advanced, or any level.
- Set a maximum course duration.
- Review the ranked matches and the topics that caused each match.

Recommendations use a simple, explainable topic-overlap score against the sample catalog in `streamlit_app.py`. The project does not call an AI API and does not collect or store learner data.

> The catalog is illustrative sample content. This prototype does not represent real course providers, enrollment, or verified course availability.

## Run locally

Requires Python 3.10 or later.

```bash
python -m venv .venv
```

Activate the virtual environment, then install and run:

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit.

## Project files

- `streamlit_app.py` — interface, sample catalog, and matching logic.
- `requirements.txt` — Python application dependency.

## License

See [LICENSE](LICENSE).
