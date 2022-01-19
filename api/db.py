from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
'''
def create_async_engine(*arg, **kw): ...
'''
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)
'''
class sessionmaker(_SessionClassMethods):
    def __init__(self, bind: Optional[Any] = ..., class_: Any = ..., autoflush: bool = ...,
        autocommit: bool = ..., expire_on_commit: bool = ...,
        info: Optional[Any] = ..., **kw) -> None: ...
FYI:
https://qiita.com/tosizo/items/86d3c60a4bb70eb1656e
'''

Base = declarative_base()
'''
About declarative_base()
FYI:
https://www.python.ambitious-engineer.com/archives/1487
'''

async def get_db():
    async with async_session() as session:
        yield session
'''
Execute connect to DB and close it
About Async with
FYI:
https://qiita.com/halhorn/items/154d8e8e1d0f39233c85

yield session:
Normally, it is expressed as session = Session (), but in this case it is an asynchronous process.
Therefore, the value is returned each time like yield.
FYI:
https://www.sejuku.net/blog/23716
'''