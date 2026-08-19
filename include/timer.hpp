// timer.hpp — utilidades de medición de tiempo (header-only).
//
// Uso:
//   Timer t;
//   ... código ...
//   std::cout << t.elapsed_ms() << " ms\n";
//
//   {
//       TIME_BLOCK("bubble sort n=10000");
//       bubble_sort(v);
//   }   // al salir del bloque imprime: [bubble sort n=10000] 123.456 ms
//
// Nota: mide con -O2 (make release) si quieres tiempos representativos.
#pragma once

#include <chrono>
#include <iostream>
#include <string>

class Timer {
public:
    Timer() : start_(Clock::now()) {}

    void reset() { start_ = Clock::now(); }

    double elapsed_ms() const {
        return std::chrono::duration<double, std::milli>(Clock::now() - start_).count();
    }

    double elapsed_us() const {
        return std::chrono::duration<double, std::micro>(Clock::now() - start_).count();
    }

    double elapsed_s() const {
        return std::chrono::duration<double>(Clock::now() - start_).count();
    }

private:
    using Clock = std::chrono::steady_clock;
    Clock::time_point start_;
};

// Imprime el tiempo transcurrido al salir del scope (RAII).
class ScopedTimer {
public:
    explicit ScopedTimer(std::string label) : label_(std::move(label)) {}
    ~ScopedTimer() { std::cerr << "[" << label_ << "] " << timer_.elapsed_ms() << " ms\n"; }

    ScopedTimer(const ScopedTimer&) = delete;
    ScopedTimer& operator=(const ScopedTimer&) = delete;

private:
    std::string label_;
    Timer timer_;
};

#define TIMER_CONCAT_INNER(a, b) a##b
#define TIMER_CONCAT(a, b) TIMER_CONCAT_INNER(a, b)
#define TIME_BLOCK(label) ScopedTimer TIMER_CONCAT(_scoped_timer_, __LINE__)(label)
