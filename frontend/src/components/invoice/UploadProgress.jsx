import { Progress } from "../ui/progress";

export default function UploadProgress({
    progress,
    filename,
}){
    return(
        <div className="space-y-2">
            <div className="flex justify-between">
                <span>
                    {filename}
                </span>
                <span>
                    {progress}%
                </span>
            </div>

            <Progress value={progress} />
            
        </div>
    );
}