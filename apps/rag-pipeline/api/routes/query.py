from fastapi import APIRouter
from pydantic import BaseModel
from actions.embed import user_query_embed
from config.logger import logger

router = APIRouter(prefix="/api", tags=["Rag"])

class QueryPayload(BaseModel):
    user_query: str

@router.post("/query")
async def query(payload: QueryPayload):
    try:
        user_query = payload.user_query
        logger.info(f"user query: {user_query}")
        results = user_query_embed(user_query)
        logger.info("top k results retieved")

        for r in results.points:
            payload = r.payload
            logger.info(
                f"score={r.score} | "
                f"video_id={payload.get('video_id')} | "
                f"start={payload.get('start_time')} | "
                f"end={payload.get('end_time')} | "
                f"text={payload.get('text')}"
            )
        return results

    except Exception as e:
        logger.error(f"Error at /query: ${e}")
        raise


@router.get("/status")
async def status():
    return {
        "status": "ok"
    }