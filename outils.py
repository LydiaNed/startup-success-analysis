from pathlib import Path
import pandas as pd

# colonnes de dates : à relire comme des dates (un CSV n'enregistre que du texte)
DATES = ["founded_at", "closed_at", "first_funding_at", "last_funding_at"]

def charger_donnees():
    """Lit data/propre.csv avec les dates correctement reconnues."""
    chemin = Path(__file__).parent / "data" / "propre.csv"
    return pd.read_csv(chemin, parse_dates=DATES)