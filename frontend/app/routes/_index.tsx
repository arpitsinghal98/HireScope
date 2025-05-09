import { Link } from "@remix-run/react";

export default function LandingPage() {
  return (
    <div className="relative min-h-screen bg-black text-white overflow-hidden flex flex-col items-center justify-center px-4">
      {/* Background spotlight gradient */}
      <div className="absolute inset-0 bg-gradient-to-r from-black via-black to-yellow-200 opacity-40 pointer-events-none" />
      
      {/* Star field background */}
      <div className="absolute inset-0 bg-[radial-gradient(#ffffff1a_1px,transparent_1px)] [background-size:20px_20px] opacity-10 pointer-events-none" />

      {/* Huge brand word */}
      <div className="w-full overflow-x-hidden flex justify-center">
        <h1 className="whitespace-nowrap text-[3.5rem] sm:text-[5rem] md:text-[8rem] lg:text-[14rem] font-extrabold text-white/10 z-10">
          HireScope
        </h1>
      </div>

      {/* Foreground content below */}
      <div className="mt-8 z-20 text-center">
        <p className="text-base sm:text-lg text-white/80 max-w-xl mx-auto mb-6 px-2">
          Track job applications and analyze ATS scores with blazing speed.
        </p>

        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <Link
            to="/browse"
            className="px-6 py-3 bg-white text-black font-semibold rounded-full hover:bg-gray-300 transition text-sm sm:text-base"
          >
            Browse Applications
          </Link>
          <Link
            to="/submit"
            className="px-6 py-3 border border-white text-white font-semibold rounded-full hover:bg-white hover:text-black transition text-sm sm:text-base"
          >
            Create New
          </Link>
        </div>
      </div>
    </div>
  );
}
