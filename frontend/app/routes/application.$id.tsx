import type { LoaderFunction } from "@remix-run/node";
import { useLoaderData, Link } from "@remix-run/react";
import { json } from "@remix-run/node";

type Application = {
  id: string;
  company_name: string;
  job_title: string;
  ats_score?: number;
  resume_url?: string;
  job_description?: string;
  created_at: string;
};

export const loader: LoaderFunction = async ({ params }) => {
  const id = params.id;
  const res = await fetch(`http://localhost:8000/api/applications/${id}`);
  if (!res.ok) throw new Response("Application not found", { status: 404 });
  const data = await res.json();
  return json(data);
};

export default function ApplicationDetail() {
  const app = useLoaderData<Application>();

  return (
    <main className="max-w-3xl mx-auto mt-10 px-4">
      <Link to="/browse" className="text-blue-600 underline mb-4 inline-block">← Back to Browse</Link>

      <h1 className="text-2xl font-bold mb-2">{app.job_title}</h1>
      <h2 className="text-xl text-gray-700 mb-4">{app.company_name}</h2>

      <p className="mb-2"><strong>ATS Score:</strong> {app.ats_score ?? "N/A"}</p>
      <p className="mb-6 text-sm text-gray-500">Created: {new Date(app.created_at).toLocaleString()}</p>

      <div className="space-y-3">
        {app.resume_url && (
          <a href={`file://${app.resume_url}`} target="_blank" rel="noopener noreferrer" className="block text-blue-600 underline">
            📄 View Resume
          </a>
        )}
        {app.job_description && (
          <a href={`file://${app.job_description}`} target="_blank" rel="noopener noreferrer" className="block text-blue-600 underline">
            📄 View JD
          </a>
        )}
      </div>
    </main>
  );
}