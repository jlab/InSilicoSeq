import numpy as np


def scale_phred_score(p_score, multiplier):
    """Scale a Phred score to increase error probability by a given multiplier.

    Args:
        p_score (int or float): Original Phred score
        multiplier (float): Factor to increase error probability (e.g., 10.0 for 10× more errors)

    Returns:
        int: Adjusted Phred score (clipped between 0 and 60)
    """
    # Apply log-based Phred scaling
    adjusted = p_score - 10 * np.log10(multiplier)

    # Clamp to valid range [0, 60]
    adjusted = max(0, min(60, round(adjusted)))

    return adjusted
