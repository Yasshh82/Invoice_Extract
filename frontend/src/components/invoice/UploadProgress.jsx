import { Progress } from "../ui/progress";

export default function UploadProgress({
    progress,
}){
    if(progress === 0) return null;

    return(
        <div className="space-y-2">

            <Progress value={progress} />

            <p className="text-sm">
                {progress}%
            </p>

        </div>
    );
}