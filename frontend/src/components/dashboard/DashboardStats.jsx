import { Card, CardContent, CardHeader, CardTitle } from "../ui/card";

export default function DashboardStats({stats}){
    return (
        <div className="grid gap-4 md:grid-cols-3">
            <Card>
                <CardHeader>
                    <CardTitle>
                        Total
                    </CardTitle>
                </CardHeader>

                <CardContent>
                    {stats.total}
                </CardContent>
            </Card>
            <Card>
                <CardHeader>
                    <CardTitle>
                        Completed
                    </CardTitle>
                </CardHeader>
                <CardContent>
                    {stats.completed}
                </CardContent>
            </Card>
            <Card>
                <CardHeader>
                    <CardTitle>
                        Failed
                    </CardTitle>
                </CardHeader>
                <CardContent>
                    {stats.failed}
                </CardContent>
            </Card>
        </div>
    );
}