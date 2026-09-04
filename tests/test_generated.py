from pathlib import Path


skill = Path("skills/kolonie/SKILL.md").read_text(encoding="utf-8")
references = Path("skills/kolonie/references")


def require(text: str) -> None:
    assert text in skill, f"SKILL.md must contain {text!r}"


assert len(skill) <= 20_000
assert (len(skill) + 3) // 4 <= 5_000

for name in (
    "academy.md",
    "browser.md",
    "incidents.md",
    "memory.md",
    "operator-handoffs.md",
    "rationale.md",
    "registration.md",
):
    assert (references / name).is_file(), f"missing generated reference: {name}"
    require(f"references/{name}")

assert len(list(references.glob("*.md"))) == 7

for text in (
    "hermes config set mcp_servers.kolonie.url",
    "kolonie.about",
    "kolonie.name.check",
    "kolonie.register",
    "confirmationToken",
    "credentials.apiKey",
    "hermes config set KOLONIE_API_KEY <the-value-from-credentials.apiKey>",
    "mcp_servers.kolonie.headers.Authorization",
    "Bearer ${KOLONIE_API_KEY}",
    "kolonie.me",
    "hermes cron create",
    "hermes cron status",
    "kolonie.wakeup",
    "~/.hermes/memories/MEMORY.md",
):
    require(text)

browser = (references / "browser.md").read_text(encoding="utf-8")
assert "browser.camofox.managed_persistence" in browser

recurring = skill[skill.index("On every authenticated session, scheduled or interactive:") :]
assert recurring.index("kolonie.wakeup") < recurring.index("kolonie.me")
assert "Load no setup reference merely because it exists" in recurring

print(
    f"generated smoke: {len(skill)} characters, "
    f"{(len(skill) + 3) // 4} approximate tokens"
)
