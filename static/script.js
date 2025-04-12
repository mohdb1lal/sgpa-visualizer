// Dark mode toggle functionality
const darkModeToggle = document.getElementById("darkModeToggle");
const body = document.body;

// Check for saved theme preference or use system preference
const savedTheme = localStorage.getItem("theme");
const prefersDark =
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: dark)").matches;

if (savedTheme === "dark" || (!savedTheme && prefersDark)) {
  body.classList.add("dark-mode");
  darkModeToggle.checked = true;
}

darkModeToggle.addEventListener("change", () => {
  body.classList.toggle("dark-mode");
  const theme = body.classList.contains("dark-mode") ? "dark" : "light";
  localStorage.setItem("theme", theme);

  // Update chart theme if it exists
  if (chart) {
    updateChartTheme();
    chart.update();
  }
});

// File upload handling
let chart = null;
let chartData = {
  labels: [],
  sgpa: [],
  cgpa: [],
};

// View state - only SGPA is shown in graph
let currentView = "sgpa";

// DOM elements
const fileInput = document.getElementById("fileInput");
const dropZone = document.getElementById("dropZone");
const uploadSection = document.getElementById("uploadSection");
const addMoreBtn = document.getElementById("addMoreBtn");

// Set up drag and drop
["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
  dropZone.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

["dragenter", "dragover"].forEach((eventName) => {
  dropZone.addEventListener(eventName, highlight, false);
});

["dragleave", "drop"].forEach((eventName) => {
  dropZone.addEventListener(eventName, unhighlight, false);
});

function highlight() {
  dropZone.classList.add("highlight");
}

function unhighlight() {
  dropZone.classList.remove("highlight");
}

dropZone.addEventListener("drop", handleDrop, false);

function handleDrop(e) {
  const files = e.dataTransfer.files;
  fileInput.files = files;
  handleFiles(files);
}

dropZone.addEventListener("click", () => {
  fileInput.click();
});

fileInput.addEventListener("change", (event) => {
  handleFiles(event.target.files);
});

addMoreBtn.addEventListener("click", () => {
  fileInput.click();
});

async function handleFiles(files) {
  if (files.length === 0) return;

  document.getElementById(
    "fileCount"
  ).textContent = `${files.length} files selected`;
  showLoading(true);

  try {
    const formData = new FormData();
    Array.from(files).forEach((file) => formData.append("files", file));

    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Upload failed");
    }

    const data = await response.json();

    // Store the data
    chartData.labels = data.semesters;
    chartData.sgpa = data.sgpa_values;
    chartData.cgpa = data.cgpa_values;

    // Update metrics
    updateMetrics();

    // Enable download button
    document.getElementById("downloadChartBtn").disabled = false;

    // Show the results container with chart and metrics
    document.getElementById("resultsContainer").style.display = "block";

    // Render the chart with SGPA only
    updateChartView();

    // Show success toast
    showToast("Grade data processed successfully!", "success");

    // Shrink the upload area and show the "Add More" button
    uploadSection.classList.add("minimized");
    addMoreBtn.style.display = "block";

    // Scroll to the results
    document
      .getElementById("resultsContainer")
      .scrollIntoView({ behavior: "smooth" });
  } catch (error) {
    showToast(error.message, "error");
  } finally {
    showLoading(false);
  }
}

function updateChartView() {
  const ctx = document.getElementById("gradeChart").getContext("2d");
  if (chart) chart.destroy();

  // Only show SGPA on the chart
  const datasets = [
    {
      label: "SGPA",
      data: chartData.sgpa,
      borderColor: body.classList.contains("dark-mode") ? "#4BC0C0" : "#4BC0C0",
      backgroundColor: body.classList.contains("dark-mode")
        ? "rgba(75, 192, 192, 0.2)"
        : "rgba(75, 192, 192, 0.2)",
      tension: 0.3,
      fill: true,
      pointRadius: 6,
      pointHoverRadius: 8,
      pointBackgroundColor: body.classList.contains("dark-mode")
        ? "#1a1a1a"
        : "#ffffff",
    },
  ];

  const fontColor = body.classList.contains("dark-mode") ? "#e0e0e0" : "#666";
  const gridColor = body.classList.contains("dark-mode")
    ? "rgba(255, 255, 255, 0.1)"
    : "rgba(0, 0, 0, 0.1)";

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: chartData.labels,
      datasets: datasets,
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          min: 0,
          max: 10,
          grid: {
            color: gridColor,
          },
          ticks: {
            color: fontColor,
          },
          title: {
            display: true,
            text: "SGPA",
            color: fontColor,
          },
        },
        x: {
          grid: {
            color: gridColor,
          },
          ticks: {
            color: fontColor,
          },
        },
      },
      plugins: {
        legend: {
          position: "top",
          labels: {
            color: fontColor,
            font: {
              size: 12,
            },
            usePointStyle: true,
            pointStyle: "circle",
          },
        },
        tooltip: {
          backgroundColor: body.classList.contains("dark-mode")
            ? "rgba(0, 0, 0, 0.8)"
            : "rgba(255, 255, 255, 0.8)",
          titleColor: body.classList.contains("dark-mode") ? "#fff" : "#333",
          bodyColor: body.classList.contains("dark-mode") ? "#fff" : "#333",
          borderColor: body.classList.contains("dark-mode")
            ? "rgba(255, 255, 255, 0.1)"
            : "rgba(0, 0, 0, 0.1)",
          borderWidth: 1,
          padding: 10,
          displayColors: true,
          callbacks: {
            label: function (context) {
              let label = context.dataset.label || "";
              if (label) {
                label += ": ";
              }
              if (context.parsed.y !== null) {
                label += context.parsed.y.toFixed(2);
              }
              return label;
            },
          },
        },
      },
      animation: {
        duration: 1500,
        easing: "easeOutQuart",
      },
    },
  });
}

function updateChartTheme() {
  if (!chart) return;

  const fontColor = body.classList.contains("dark-mode") ? "#e0e0e0" : "#666";
  const gridColor = body.classList.contains("dark-mode")
    ? "rgba(255, 255, 255, 0.1)"
    : "rgba(0, 0, 0, 0.1)";

  chart.options.scales.y.grid.color = gridColor;
  chart.options.scales.x.grid.color = gridColor;
  chart.options.scales.y.ticks.color = fontColor;
  chart.options.scales.x.ticks.color = fontColor;
  chart.options.scales.y.title.color = fontColor;
  chart.options.plugins.legend.labels.color = fontColor;
  chart.options.plugins.tooltip.backgroundColor = body.classList.contains(
    "dark-mode"
  )
    ? "rgba(0, 0, 0, 0.8)"
    : "rgba(255, 255, 255, 0.8)";
  chart.options.plugins.tooltip.titleColor = body.classList.contains(
    "dark-mode"
  )
    ? "#fff"
    : "#333";
  chart.options.plugins.tooltip.bodyColor = body.classList.contains("dark-mode")
    ? "#fff"
    : "#333";

  chart.data.datasets.forEach((dataset) => {
    dataset.pointBackgroundColor = body.classList.contains("dark-mode")
      ? "#1a1a1a"
      : "#ffffff";
  });
}

function updateMetrics() {
  // Update current CGPA
  const cgpaValues = chartData.cgpa.filter((val) => val !== null);
  const currentCGPA =
    cgpaValues.length > 0 ? cgpaValues[cgpaValues.length - 1] : null;

  document.getElementById("current-cgpa").textContent =
    currentCGPA !== null ? currentCGPA.toFixed(2) : "-";

  // Update latest SGPA
  const sgpaValues = chartData.sgpa.filter((val) => val !== null);
  const latestSGPA =
    sgpaValues.length > 0 ? sgpaValues[sgpaValues.length - 1] : null;

  document.getElementById("latest-sgpa").textContent =
    latestSGPA !== null ? latestSGPA.toFixed(2) : "-";

  // Update semester count
  const semesterCount = sgpaValues.length;
  document.getElementById("semester-count").textContent = semesterCount;
}

function showLoading(show) {
  const loadingOverlay = document.getElementById("chartLoading");
  if (show) {
    loadingOverlay.style.display = "flex";
  } else {
    loadingOverlay.style.display = "none";
  }
}

// Download chart as image
document.getElementById("downloadChartBtn").addEventListener("click", () => {
  if (!chart) return;

  const canvas = document.getElementById("gradeChart");
  const image = canvas.toDataURL("image/png", 1.0);

  const link = document.createElement("a");
  link.download = "academic-progress-chart.png";
  link.href = image;
  link.click();

  showToast("Chart downloaded successfully!", "success");
});

// Toast notification
function showToast(message, type = "success") {
  const toast = document.getElementById("toast");
  const toastMessage = document.querySelector(".toast-message");
  const icon = toast.querySelector("i");

  // Set type-specific styling
  toast.className = "toast";
  toast.classList.add(type);

  // Set icon based on type
  icon.className = "fas";
  if (type === "success") icon.classList.add("fa-check-circle");
  else if (type === "error") icon.classList.add("fa-exclamation-circle");
  else if (type === "info") icon.classList.add("fa-info-circle");
  else if (type === "warning") icon.classList.add("fa-exclamation-triangle");

  // Set message
  toastMessage.textContent = message;

  // Show toast
  toast.classList.add("show");

  // Hide after 3 seconds
  setTimeout(() => {
    toast.classList.remove("show");
  }, 3000);
}
