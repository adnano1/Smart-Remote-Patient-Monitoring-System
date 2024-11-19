import React from 'react';
import { Line } from 'react-chartjs-2';

function HealthPrediction({ predictionData }) {
    const chartData = {
        labels: predictionData.map(d => d.timestamp),
        datasets: [
            {
                label: 'Predicted Heart Rate',
                data: predictionData.map(d => d.predicted_heart_rate),
                borderColor: 'rgba(54, 162, 235, 1)',
                fill: false,
            }
        ],
    };

    return (
        <div>
            <h2>Health Prediction</h2>
            <Line data={chartData} />
        </div>
    );
}

export default HealthPrediction;
