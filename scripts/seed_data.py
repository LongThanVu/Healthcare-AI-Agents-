from __future__ import annotations

import asyncio

from shared.database.seed import seed_reference_data
from shared.database.session import get_session_factory, init_db


async def main() -> None:
    await init_db()
    async with get_session_factory()() as session:
        await seed_reference_data(session)
    print("Database initialized and sample data seeded.")


if __name__ == "__main__":
    asyncio.run(main())
