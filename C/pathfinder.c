#include "raylib.h"
#include <float.h>

void plotpath(float x_pos_list[], float y_pos_list[], int length)
{
    const int screenWidth = 800;
    const int screenHeight = 700;

    InitWindow(screenWidth, screenHeight, "position tracker");
    SetTargetFPS(60);

    // Find the limits of the data
    float minX = FLT_MAX;
    float maxX = -FLT_MAX;
    float minY = FLT_MAX;
    float maxY = -FLT_MAX;

    for (int i = 0; i < length; i++)
    {
        if (x_pos_list[i] < minX) minX = x_pos_list[i];
        if (x_pos_list[i] > maxX) maxX = x_pos_list[i];

        if (y_pos_list[i] < minY) minY = y_pos_list[i];
        if (y_pos_list[i] > maxY) maxY = y_pos_list[i];
    }

    // Add some space around the graph
    float paddingX = (maxX - minX) * 0.1f;
    float paddingY = (maxY - minY) * 0.1f;

    if (paddingX == 0) paddingX = 1;
    if (paddingY == 0) paddingY = 1;

    minX -= paddingX;
    maxX += paddingX;
    minY -= paddingY;
    maxY += paddingY;

    // Graph area
    float left = 70;
    float right = 30;
    float top = 60;
    float bottom = 60;

    float graphWidth = screenWidth - left - right;
    float graphHeight = screenHeight - top - bottom;

    while (!WindowShouldClose())
    {
        BeginDrawing();

        ClearBackground(RAYWHITE);

        // -------------------------
        // Draw grid
        // -------------------------

        int gridLines = 10;

        for (int i = 0; i <= gridLines; i++)
        {
            float x = left + (graphWidth * i / gridLines);
            float y = top + (graphHeight * i / gridLines);

            DrawLine(
                (int)x,
                (int)top,
                (int)x,
                (int)(top + graphHeight),
                LIGHTGRAY
            );

            DrawLine(
                (int)left,
                (int)y,
                (int)(left + graphWidth),
                (int)y,
                LIGHTGRAY
            );
        }

        // -------------------------
        // Convert physics coordinates
        // to screen coordinates
        // -------------------------

        for (int i = 0; i < length - 1; i++)
        {
            float screenX1 =
                left +
                ((x_pos_list[i] - minX) / (maxX - minX)) * graphWidth;

            float screenY1 =
                top +
                graphHeight -
                ((y_pos_list[i] - minY) / (maxY - minY)) * graphHeight;

            float screenX2 =
                left +
                ((x_pos_list[i + 1] - minX) / (maxX - minX)) * graphWidth;

            float screenY2 =
                top +
                graphHeight -
                ((y_pos_list[i + 1] - minY) / (maxY - minY)) * graphHeight;

            // Path
            DrawLineEx(
                (Vector2){screenX1, screenY1},
                (Vector2){screenX2, screenY2},
                1.0f,
                (Color){78, 191, 217, 255}
            );

            // Marker
            DrawCircle(
                (int)screenX1,
                (int)screenY1,
                2,
                (Color){78, 191, 217, 255}
            );
        }

        // -------------------------
        // Starting position
        // -------------------------

        float startX =
            left +
            ((x_pos_list[0] - minX) / (maxX - minX)) * graphWidth;

        float startY =
            top +
            graphHeight -
            ((y_pos_list[0] - minY) / (maxY - minY)) * graphHeight;

        DrawCircle(
            (int)startX,
            (int)startY,
            7,
            GREEN
        );

        DrawText(
            "START",
            (int)startX + 10,
            (int)startY - 10,
            20,
            BLACK
        );

        // -------------------------
        // Labels
        // -------------------------

        DrawText(
            "X-axis",
            screenWidth / 2 - 30,
            screenHeight - 35,
            20,
            BLACK
        );

        DrawText(
            "Y-axis",
            15,
            screenHeight / 2 - 10,
            20,
            BLACK
        );

        DrawText(
            "position tracker",
            screenWidth / 2 - 90,
            20,
            25,
            BLACK
        );

        // Legend
        DrawLineEx(
            (Vector2){screenWidth - 180, 30},
            (Vector2){screenWidth - 150, 30},
            2,
            (Color){78, 191, 217, 255}
        );

        DrawText(
            "object path",
            screenWidth - 140,
            20,
            20,
            BLACK
        );

        EndDrawing();
    }

    CloseWindow();
}