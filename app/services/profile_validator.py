def validate_profiles(data):
    if not isinstance(data, dict):
        raise ValueError("Root must be an object")

    for profile_id, langs in data.items():
        if not isinstance(langs, dict):
            raise ValueError(f"{profile_id} must be an object")

        for lang, fields in langs.items():
            if "name" not in fields:
                raise ValueError(f"[{profile_id}.{lang}] Missing name")

            # Experience & Motivation are OPTIONAL
            if "Exprience" not in fields:
                fields["Exprience"] = ""

            if "Motivation" not in fields:
                fields["Motivation"] = ""
