from fastapi import FastAPI, Form, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from contextlib import asynccontextmanager
from database.main import get_session, create_all_tables
from application.main import handle_application_process
from api.routes import application as application_router

# ✅ Define startup/shutdown logic here
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_tables()  # ← runs at startup
    yield  # ← everything after this would run on shutdown (if needed)

# ✅ Initialize FastAPI with lifespan context
app = FastAPI(lifespan=lifespan)

app.include_router(application_router.router, prefix="/api")

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can scope this down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Application creation endpoint
@app.post("/api/applications")
def submit_application(
    company_name: str = Form(...),
    job_title: str = Form(...),
    jd_text: str = Form(...),
    resume: UploadFile = Form(...),
    session: Session = Depends(get_session)
):
    app_record = handle_application_process(
        session=session,
        company_name=company_name,
        job_title=job_title,
        resume_file=resume,
        jd_text=jd_text
    )
    return app_record