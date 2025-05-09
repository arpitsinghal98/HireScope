import { Form, useNavigation, useActionData } from "@remix-run/react";

type ActionData = {
  error?: string;
};
import type { ActionFunction } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";

// 👇 Action to POST form data to FastAPI backend
export const action: ActionFunction = async ({ request }) => {
  const formData = await request.formData();

  const response = await fetch("http://localhost:8000/api/applications", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    return json({ error: "Failed to submit application." }, { status: 500 });
  }

  const data = await response.json();

  // ✅ Option 1: Redirect to detail page after submission
  return redirect(`/application/${data.id}`);

  // ✅ Option 2 (alternative): return data and show confirmation
  // return json({ success: true, id: data.id, score: data.ats_score });
};
export default function SubmitApplication() {
  const navigation = useNavigation();
  const isSubmitting = navigation.state === "submitting";
  const actionData = useActionData<ActionData>();

  return (
    <div className="max-w-2xl mx-auto mt-10">
      <h1 className="text-2xl font-bold mb-6">Submit Application</h1>

      {actionData?.error && (
        <div className="mb-4 text-red-600">{actionData.error}</div>
      )}

      <Form method="post" encType="multipart/form-data">
        <label htmlFor="company_name" className="block mb-2">Company Name</label>
        <input id="company_name" type="text" name="company_name" className="w-full p-2 border mb-4" required />

        <label htmlFor="job_title" className="block mb-2">Job Title</label>
        <input id="job_title" type="text" name="job_title" className="w-full p-2 border mb-4" required />

        <label htmlFor="jd_text" className="block mb-2">Job Description</label>
        <textarea id="jd_text" name="jd_text" rows={10} className="w-full p-2 border mb-4" required />

        <label htmlFor="resume" className="block mb-2">Upload Resume (PDF)</label>
        <input id="resume" type="file" name="resume" accept="application/pdf" className="mb-6" required />

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Submitting..." : "Submit"}
        </button>
      </Form>
    </div>
  );
}