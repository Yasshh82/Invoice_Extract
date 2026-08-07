import { Progress } from "@/components/ui/progress";

export default function BatchProgress({ progress }) {
    return (
        <div className="space-y-2">
            <Progress value={progress.percentage} />
            <p>
                {progress.completed}/{progress.total}
            </p>
        </div>
    );
}
