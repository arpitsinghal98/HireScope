import { json, LoaderFunction } from "@remix-run/node";
import { useLoaderData, Link } from "@remix-run/react";

type Application = {
  id: string;
  company_name: string;
  job_title: string;
  ats_score?: number;
  created_at: string;
};

export const loader: LoaderFunction = async () => {
  const res = await fetch("http://localhost:8000/api/applications");
  const data = await res.json();
  return json(data);
};

export default function BrowseApplications() {
  const apps = useLoaderData<Application[]>();

  return (
    <main className="max-w-4xl mx-auto mt-10 px-4">
      <h1 className="text-2xl font-bold mb-6">All Applications</h1>

      {apps.length === 0 ? (
        <p className="text-gray-500">No applications found.</p>
      ) : (
        <div className="grid gap-4">
          {apps.map((app) => (
            <Link
              key={app.id}
              to={`/application/${app.id}`}
              className="block border p-4 rounded-xl shadow hover:shadow-md transition bg-white"
            >
              <div className="flex justify-between">
                <div>
                  <h2 className="text-lg font-semibold">{app.company_name}</h2>
                  <p className="text-gray-600">{app.job_title}</p>
                </div>
                <div className="text-right text-sm text-gray-500">
                  <p>ATS Score: <strong>{app.ats_score ?? "N/A"}</strong></p>
                  <p>{new Date(app.created_at).toLocaleDateString()}</p>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </main>
  );
}