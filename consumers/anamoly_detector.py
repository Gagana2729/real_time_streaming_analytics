def detect_anomaly(value, mean, std):
    if std == 0:
        return False

    z = (value - mean) / std

    if abs(z) > 2:
        return True

    return False