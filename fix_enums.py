"""Gemini only accepts string enums in tool schemas. Convert int enums to strings.

Use in /a0/helpers/litellm_transport.py, just before `iterator = await aresponses(**request)`:

    from fix_enums import fix_enums
    fix_enums(request.get("tools"))
"""


def fix_enums(o):
    if isinstance(o, dict):
        if "enum" in o and any(not isinstance(v, str) for v in o["enum"]):
            o["enum"] = [str(v) for v in o["enum"]]
            o["type"] = "string"
        for v in o.values():
            fix_enums(v)
    elif isinstance(o, list):
        for v in o:
            fix_enums(v)
