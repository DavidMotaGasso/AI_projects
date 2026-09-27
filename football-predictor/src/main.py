import os
import asyncio
from datetime import date
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

load_dotenv()

today = date.today().strftime("%Y-%m-%d")

options = ClaudeAgentOptions(
    model="claude-haiku-4-5-20251001",
    allowed_tools=["WebSearch"],
    disallowed_tools=["WebFetch"],
    max_turns=3
)

prompt = f"""
Today's date is {today}.

Search site:marca.com ONLY for Girona FC's last 5 completed matches in
LaLiga Hypermotion 2026/27 (Spanish Segunda División).

STRICT RULES:
- Only use results from the as.com domain.
- Only include official LaLiga Hypermotion 2026/27 league matches.
- Do NOT include Copa del Rey, friendlies, or any other competition.
- Do a single targeted search. Use the first reliable result you find;
  do not cross-check across multiple sources.

Return ONLY a table with these exact columns, nothing else:
| Matchday | Date | Opponent | Home/Away | Score | Source URL |
"""

async def main():
    print("Starting call to Claude...")
    async for message in query(prompt=prompt, options=options):
        print("Message received:", message)
    print("Call finished.")

if __name__ == "__main__":
    asyncio.run(main())