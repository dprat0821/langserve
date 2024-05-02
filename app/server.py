from fastapi import FastAPI
from langserve import add_routes
from pirate_speak.chain import chain as pirate_speak_chain


app = FastAPI()

add_routes(
    app,
    pirate_speak_chain,
    path="/mine",
    playground_type="chat",
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True,
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
