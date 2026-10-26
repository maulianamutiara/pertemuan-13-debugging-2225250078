
def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


print("Status 59:", status_lulus(59))
print("Status 60:", status_lulus(60))
print("Status 61:", status_lulus(61))
