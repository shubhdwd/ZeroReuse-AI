def route_prompt(prompt: str):
    p = prompt.lower()

    # AI model (Replicate)
    if "cartoon" in p:
        return "cartoon"

    # OpenCV features
    if "vintage" in p or "sepia" in p:
        return "vintage"

    if "dramatic" in p:
        return "dramatic"

    if "cinematic" in p:
        return "cinematic"

    if "studio" in p or "clarity" in p or "enhance" in p or "improve" in p:
        return "studio"

    if "soft portrait" in p or "portrait" in p:
        return "portrait"

    if "cyberpunk" in p or "neon" in p:
        return "cyberpunk"

    if "minimal" in p:
        return "minimal"

    if "black" in p or "noir" in p:
        return "bw"

    if "blur" in p or "privacy" in p:
        return "face_blur"
    
    if "gender" in p or "male" in p or "female" in p:
        return "gender_swap"

    return "default"
